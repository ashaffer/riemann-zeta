import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk3 :
    P2RoundedFactorCheckpointData.panel12Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix12_eq :
    P2RoundedFactorCheckpointData.panel12Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk3.1

theorem panel12Prefix13_eq :
    P2RoundedFactorCheckpointData.panel12Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk3.2.1

theorem panel12Prefix14_eq :
    P2RoundedFactorCheckpointData.panel12Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk3.2.2.1

theorem panel12Prefix15_eq :
    P2RoundedFactorCheckpointData.panel12Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk3.2.2.2

end RHP2Bridge
