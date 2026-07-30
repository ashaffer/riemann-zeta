import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel2FlatEven3 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven3 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel2FlatComponentChunk3

end RHP2Bridge
