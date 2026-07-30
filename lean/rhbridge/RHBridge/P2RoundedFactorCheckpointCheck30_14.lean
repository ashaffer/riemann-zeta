import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk14 :
    P2RoundedFactorCheckpointData.panel30Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix56_eq :
    P2RoundedFactorCheckpointData.panel30Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk14.1

theorem panel30Prefix57_eq :
    P2RoundedFactorCheckpointData.panel30Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk14.2.1

theorem panel30Prefix58_eq :
    P2RoundedFactorCheckpointData.panel30Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk14.2.2.1

theorem panel30Prefix59_eq :
    P2RoundedFactorCheckpointData.panel30Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk14.2.2.2

end RHP2Bridge
