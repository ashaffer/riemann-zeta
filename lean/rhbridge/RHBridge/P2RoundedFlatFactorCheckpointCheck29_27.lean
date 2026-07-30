import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel29FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel29FlatComponentChunk27

end RHP2Bridge
