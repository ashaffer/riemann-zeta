import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel18FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel18FlatComponentChunk38

end RHP2Bridge
