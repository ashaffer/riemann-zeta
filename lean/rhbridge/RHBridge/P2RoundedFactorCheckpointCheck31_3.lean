import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk3 :
    P2RoundedFactorCheckpointData.panel31Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix12_eq :
    P2RoundedFactorCheckpointData.panel31Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk3.1

theorem panel31Prefix13_eq :
    P2RoundedFactorCheckpointData.panel31Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk3.2.1

theorem panel31Prefix14_eq :
    P2RoundedFactorCheckpointData.panel31Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk3.2.2.1

theorem panel31Prefix15_eq :
    P2RoundedFactorCheckpointData.panel31Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk3.2.2.2

end RHP2Bridge
