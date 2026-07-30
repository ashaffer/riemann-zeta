import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel2FlatEven0 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven0 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel2FlatComponentChunk0

end RHP2Bridge
