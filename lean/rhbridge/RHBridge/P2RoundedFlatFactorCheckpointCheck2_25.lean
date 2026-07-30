import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel2FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel2FlatComponentChunk25

end RHP2Bridge
