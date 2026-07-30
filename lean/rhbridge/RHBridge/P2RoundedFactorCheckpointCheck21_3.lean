import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk3 :
    P2RoundedFactorCheckpointData.panel21Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix12_eq :
    P2RoundedFactorCheckpointData.panel21Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk3.1

theorem panel21Prefix13_eq :
    P2RoundedFactorCheckpointData.panel21Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk3.2.1

theorem panel21Prefix14_eq :
    P2RoundedFactorCheckpointData.panel21Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk3.2.2.1

theorem panel21Prefix15_eq :
    P2RoundedFactorCheckpointData.panel21Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk3.2.2.2

end RHP2Bridge
