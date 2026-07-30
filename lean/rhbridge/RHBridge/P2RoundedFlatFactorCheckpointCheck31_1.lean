import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel31FlatEven1 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel31FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel31FlatEven1 =
      (P2RoundedFactorCheckpointData.panel31TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel31FlatComponentChunk1

end RHP2Bridge
