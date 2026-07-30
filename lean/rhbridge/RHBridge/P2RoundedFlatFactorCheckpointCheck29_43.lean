import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel29FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel29FlatComponentChunk43

end RHP2Bridge
