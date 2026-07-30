import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk14 :
    P2RoundedFactorCheckpointData.panel11Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix56_eq :
    P2RoundedFactorCheckpointData.panel11Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk14.1

theorem panel11Prefix57_eq :
    P2RoundedFactorCheckpointData.panel11Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk14.2.1

theorem panel11Prefix58_eq :
    P2RoundedFactorCheckpointData.panel11Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk14.2.2.1

theorem panel11Prefix59_eq :
    P2RoundedFactorCheckpointData.panel11Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk14.2.2.2

end RHP2Bridge
