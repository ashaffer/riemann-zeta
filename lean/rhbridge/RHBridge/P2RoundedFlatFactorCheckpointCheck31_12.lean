import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel31FlatEven12 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel31FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel31FlatEven12 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel31FlatComponentChunk12

end RHP2Bridge
