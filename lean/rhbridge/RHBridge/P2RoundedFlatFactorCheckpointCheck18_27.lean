import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel18FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel18FlatComponentChunk27

end RHP2Bridge
