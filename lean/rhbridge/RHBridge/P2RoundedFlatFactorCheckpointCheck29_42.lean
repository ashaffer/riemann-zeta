import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel29FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel29FlatComponentChunk42

end RHP2Bridge
