import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel18FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel18FlatComponentChunk42

end RHP2Bridge
