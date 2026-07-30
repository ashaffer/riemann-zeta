import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk3 :
    P2RoundedFactorCheckpointData.panel30Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix12_eq :
    P2RoundedFactorCheckpointData.panel30Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk3.1

theorem panel30Prefix13_eq :
    P2RoundedFactorCheckpointData.panel30Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk3.2.1

theorem panel30Prefix14_eq :
    P2RoundedFactorCheckpointData.panel30Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk3.2.2.1

theorem panel30Prefix15_eq :
    P2RoundedFactorCheckpointData.panel30Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk3.2.2.2

end RHP2Bridge
