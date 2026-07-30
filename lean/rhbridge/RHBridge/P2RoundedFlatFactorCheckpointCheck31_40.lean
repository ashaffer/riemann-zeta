import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel31FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel31FlatComponentChunk40

end RHP2Bridge
