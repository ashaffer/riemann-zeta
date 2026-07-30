import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel29FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel29FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel29FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel29TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel29FlatComponentChunk46

end RHP2Bridge
