import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel18FlatEven0 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel18FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel18FlatEven0 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel18FlatComponentChunk0

end RHP2Bridge
