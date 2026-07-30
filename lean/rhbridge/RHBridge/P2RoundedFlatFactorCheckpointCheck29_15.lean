import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel29FlatEven15 =
      (P2RoundedFactorCheckpointData.panel29TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel29FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel29FlatEven15 =
      (P2RoundedFactorCheckpointData.panel29TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel29FlatComponentChunk15

end RHP2Bridge
