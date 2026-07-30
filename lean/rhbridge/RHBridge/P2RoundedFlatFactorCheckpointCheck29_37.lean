import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel29FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel29FlatComponentChunk37

end RHP2Bridge
