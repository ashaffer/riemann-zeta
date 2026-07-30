import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel18FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel18FlatComponentChunk25

end RHP2Bridge
