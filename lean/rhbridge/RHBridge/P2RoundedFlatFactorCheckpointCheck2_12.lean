import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel2FlatEven12 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven12 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel2FlatComponentChunk12

end RHP2Bridge
